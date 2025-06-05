# PharmaMongoDB

## Project Overview

PharmaMongoDB is a sample project demonstrating how to store and analyze
pharmaceutical data using MongoDB. The repository contains a Python script for
preparing the data along with example queries for exploring the database.

## Running `data_wrangling.py`

The `data_wrangling.py` script prepares the raw dataset and loads it into a
MongoDB instance.

### Dependencies

- Python 3.8+
- `pymongo`

Install the dependency with:

```bash
pip install pymongo
```

### Example command

```bash
python data_wrangling.py --input data/pharma.csv --db pharma_db
```

Replace `data/pharma.csv` with the path to your dataset and `pharma_db` with the
name of the MongoDB database you want to create or update.

## Executing MongoDB Queries

After running `data_wrangling.py`, start a MongoDB shell and connect to your
database:

```bash
mongo pharma_db
```

You can then execute queries such as:

```javascript
db.prescriptions.find({ drug: "aspirin" })
```

Modify the queries as needed to explore your data.

## Dataset Requirements

The data wrangling script assumes a CSV file containing prescription
information. Required columns are:

- `patient_id`
- `drug`
- `quantity`
- `date`

Other fields are optional but can be included.

