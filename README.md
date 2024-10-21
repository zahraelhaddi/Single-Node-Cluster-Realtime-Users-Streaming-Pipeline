# Single-Node-Cluster-Realtime-Users-Streaming-Pipeline
Single Node Cluster for the first part of the comparative analysis of Single node and MultiNode Kafka and spark Clusters
Got it! Here’s a revised README that provides a more comprehensive overview of the project, including explanations of Airflow, the data being processed, the architecture used, and the project’s goals.

```markdown
# Document Intake & Understanding Component

## Overview
The Document Intake & Understanding Component is designed to automate the collection and organization of essential documents from fund-seekers. The goal is to streamline the processing of these documents, enabling efficient data extraction and analysis. The system uses a microservices architecture to ensure scalability and maintainability.

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
4. **Data Storage**: Processed data is stored in PostgreSQL, making it readily accessible for further analysis or reporting.

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
   - **Airflow Web UI**: Navigate to [http://localhost:8080](http://localhost:8080) to monitor and manage workflows.
   - **PostgreSQL**: Access it on `localhost:5432` (default credentials: user: `airflow`, password: `airflow`).
   - **Grafana**: View at [http://localhost:3000](http://localhost:3000) to monitor system metrics.

### Initial Configuration

- **Database Setup**:
   - Open the Airflow web UI.
   - Under the **Admin** tab, configure necessary connections to PostgreSQL if needed.

- **Run Workflows**:
   - Create and execute initial workflows within Airflow to start processing documents. 

## Project Goal
The primary objective of this project is to develop a robust pipeline that efficiently processes documents submitted by fund-seekers, enabling the extraction of valuable insights and maintaining data integrity. By automating the workflow with Apache Airflow and using Kafka for real-time data handling, the project aims to reduce manual intervention and improve processing speed.

## Monitoring
Prometheus and Grafana are integrated for system monitoring. You can visualize system metrics and health through Grafana to ensure that all components are functioning optimally.

## Contributing
To contribute to this project, please fork the repository, create a new branch, and submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments
Special thanks to the communities behind the technologies used in this project.
```

### Instructions for Use:
1. Replace `yourusername/repository-name` with your actual GitHub username and the repository name.
2. Adjust any sections based on your specific project details or additional components you want to highlight.

Feel free to ask for any further modifications or additional details!
