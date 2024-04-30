import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from src.core.constants import IN_FOLDER
from src.services import FlightProcessor
from src.db.session import SessionLocal

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)


class MonitoringHandler(FileSystemEventHandler):
    def __init__(self, flight_processor: FlightProcessor):
        super().__init__()
        self.flight_processor = flight_processor

    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith(".csv"):
            logging.info(f"New file detected: {event.src_path}")
            self.flight_processor.process_file(event.src_path)


def start_monitoring():
    path = IN_FOLDER
    observer = Observer()
    db_session = SessionLocal()
    flight_processor = FlightProcessor(db_session)
    event_handler = MonitoringHandler(flight_processor)
    observer.schedule(event_handler, path)
    observer.start()
    logging.info("Monitoring started...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    start_monitoring()
