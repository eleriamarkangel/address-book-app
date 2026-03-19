import logging
import os

# Create logs directory if it doesn't exist
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# Define log file path (single file)
log_file = os.path.join(log_dir, "app.log")

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        # File handler - logs to file
        logging.FileHandler(log_file),
        # Console handler - logs to stdout
        logging.StreamHandler()
    ]
)

# Get logger instance
logger = logging.getLogger(__name__)

# Log that logger is initialized
logger.info(f"Logger initialized. Log file: {log_file}")
