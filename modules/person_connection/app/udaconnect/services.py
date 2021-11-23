import logging
from datetime import datetime, timedelta
from typing import Dict, List
import json
from app import db
from app.udaconnect.models import Connection, Person, Location
from app.udaconnect.schemas import ConnectionSchema, PersonSchema, LocationSchema
from geoalchemy2.functions import ST_AsText, ST_Point
from sqlalchemy.sql import text
from kafka import KafkaProducer
from flask import jsonify
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger("personal-connections-api")
TOPIC_NAME = 'ServicesUdaConnect'
KAFKA_SERVER = 'kafka.default.svc.cluster.local:9092'
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)
class ConnectionService:
    @staticmethod
    def find_contacts(person_id: int, start_date: datetime, end_date: datetime, meters=5
    ) -> List[Connection]:
        locations: List = db.session.query(Location).filter(
            Location.person_id == person_id
        ).filter(Location.creation_time < end_date).filter(
            Location.creation_time >= start_date
        ).all()
        person_map: Dict[str, Person] = {person.id: person for person in PersonService.retrieve_all()}
        data = []
        for location in locations:
            data.append(
                {
                    "person_id": person_id,
                    "longitude": location.longitude,
                    "latitude": location.latitude,
                    "meters": meters,
                    "start_date": start_date.strftime("%Y-%m-%d"),
                    "end_date": (end_date + timedelta(days=1)).strftime("%Y-%m-%d"),
                }
            )

        query = text(
        )
        result: List[Connection] = []
        for line in tuple(data):
            for (
                exposed_person_id,
                location_id,
                exposed_lat,
                exposed_long,
                exposed_time,
            ) in db.engine.execute(query, **line):
                location = Location(
                    id=location_id,
                    person_id=exposed_person_id,
                    creation_time=exposed_time,
                )
                location.set_wkt_with_coords(exposed_lat, exposed_long)

                result.append(
                    Connection(
                        person=person_map[exposed_person_id], location=location,
                    )
                )
        return result
class PersonService:
    @staticmethod
    def create(person: Dict) -> Person:
        new_person = json.dumps(person).encode()
        producer.send(TOPIC_NAME, new_person)
        producer.flush()
        return "Request Sent!"
    @staticmethod
    def retrieve(person_id: int) -> Person:
        person = db.session.query(Person).get(person_id)
        return person

    @staticmethod
    def retrieve_all() -> List[Person]:
        result = db.session.query(Person).all()
        
        return result