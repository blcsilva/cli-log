import os
import sys
import tarfile
from datetime import datetime

def archive_logs(log_directory):
    # Create a new directory for archived logs if it doesn't exist
    archive_directory = os.path.join(log_directory, 'archive')
    os.makedirs(archive_directory, exist_ok=True)

    # Create the filename for the tar.gz file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_filename = f"logs_archive_{timestamp}.tar.gz"
    archive_path = os.path.join(archive_directory, archive_filename)

    # Compress the logs
    with tarfile.open(archive_path, "w:gz") as tar:
        for log_file in os.listdir(log_directory):
            log_file_path = os.path.join(log_directory, log_file)
            if os.path.isfile(log_file_path):
                tar.add(log_file_path, arcname=log_file)
    
    # Log the date and time of the archive
    log_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(os.path.join(archive_directory, "archive_log.txt"), "a") as log_file:
        log_file.write(f"Archived logs at {log_timestamp} to {archive_filename}\n")
    
    print(f"Logs archived successfully: {archive_path}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: log-archive <log-directory>")
        sys.exit(1)

    log_directory = sys.argv[1]

    if not os.path.isdir(log_directory):
        print(f"Error: {log_directory} is not a valid directory.")
        sys.exit(1)

    archive_logs(log_directory)
