# Single-Node-Cluster-Realtime-Users-Streaming-Pipeline
Single Node Cluster for the first part of the comparative analysis of Single node and MultiNode Kafka and spark Clusters
The objectif of this part1 is to analyze the performance of a single node cluster (both for kafka and Spark) in streaming and processing data coming from an API to a Cassandra.


## Architecture
This project employs a microservices architecture, utilizing the following components:

- **Apache Kafka**: Serves as the messaging backbone, facilitating real-time data streaming between services.
- **Apache Airflow**: Manages and orchestrates complex workflows, allowing for automated execution of data processing tasks.
- **PostgreSQL**: Acts as the primary data storage solution, holding processed information for easy retrieval and analysis.
- **Prometheus and Grafana**: Used for monitoring the health and performance of the system, providing insights into metrics and alerts.

### Data Flow
1. **Document Upload**: Fund-seekers submit documents, which are collected by the system.
2. **Message Queue**: Kafka handles the ingestion of these documents, ensuring reliable and scalable data processing.
3. **Workflow Management**: Airflow orchestrates the workflows to extract, transform, and load (ETL) data from the uploaded documents into PostgreSQL.
4. **Data Storage**: Processed data is stored in Cassandra, making it readily accessible for further analysis or reporting.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) and [Docker Compose](https://docs.docker.com/compose/) must be installed on your machine.

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/repository-name.git
   cd repository-name
   ```

2. **Start the Services**:
   Use the following command to build and run the Docker containers defined in the `docker-compose.yml` file:
   ```bash
   docker-compose up --build
   ```

3. **Access the Services**:
   - **Airflow Web UI**: Serves as the messaging backbone, facilitating real-time data streaming between services.
   - **Kafka**: Enabling asynchronous pub-sub system (producers: API, Consumers: Spark).
   - **Spark**: Processing API data from kafka topics.
   - **Cassandra**: to Store Processed API data.
   - **Prometheus**: to retreive & monitor kafka cluster metrics. 
   - **Grafana**: View at [http://localhost:3000](http://localhost:3000) to monitor system metrics using prometheus as a data source.
   - **PostgreSQL**: the metadata database for Airflow. It stores essential information related to workflows, such as task instances, execution dates, logs.

### Initial Configuration

- **Run Workflows**:
   - Create and execute initial workflows within Airflow to start processing documents. 

## Monitoring
Prometheus and Grafana are integrated for system monitoring. You can visualize system metrics and health through Grafana to ensure that all components are functioning optimally.

## Contributing
To contribute to this project, please fork the repository, create a new branch, and submit a pull request.


```
