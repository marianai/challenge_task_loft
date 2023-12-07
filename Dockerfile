# Python image
FROM python:3.8

# Working directory in the container
WORKDIR /challenge

# Copy into the container at /challenge
COPY . /challenge

# Install packages from document
RUN pip install --no-cache-dir -r package.txt

# Install cron
RUN apt-get update && apt-get install -y cron

# Add a cron job 
RUN echo "*/5 * * * * cd /challenge && python post_entry.py >> /var/log/post_entry.log 2>&1" > /etc/cron.d/cron_job

# Give execution rights 
RUN chmod 0644 /etc/cron.d/cron_job

# Run the cron daemon and the command on container startup
CMD ["cron", "-f"]