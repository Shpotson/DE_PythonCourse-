from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, to_timestamp, hour
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType, TimestampType
from kafka import KafkaProducer
import psycopg2
import time
