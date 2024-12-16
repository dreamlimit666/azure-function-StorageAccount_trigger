import logging
import azure.functions as func
from pymongo import MongoClient
import json

# MongoDB connection string
MONGO_CONNECTION_STRING = ""
DATABASE_NAME = "datalog"
COLLECTION_NAME = "log"

# Initialize MongoDB client
client = MongoClient(MONGO_CONNECTION_STRING)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

app = func.FunctionApp()

@app.event_grid_trigger(arg_name="azeventgrid")
def EventGridTrigger(azeventgrid: func.EventGridEvent):
    logging.info('Python EventGrid trigger processed an event')

    # Parse the event data
    event_data = azeventgrid.get_json()
    logging.info(f"Event data: {event_data}")

    try:
        # Prepare a document to insert into MongoDB
        document = {
            "event_id": azeventgrid.id,
            "event_type": azeventgrid.event_type,
            "subject": azeventgrid.subject,
            "data": event_data,
            "event_time": azeventgrid.event_time.isoformat()
        }

        # Insert the document into MongoDB
        result = collection.insert_one(document)
        logging.info(f"Inserted document with ID: {result.inserted_id}")
    except Exception as e:
        logging.error(f"Failed to process event: {e}")
