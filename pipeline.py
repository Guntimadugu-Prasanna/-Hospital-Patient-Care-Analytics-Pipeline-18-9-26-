from extract import extract_data
from transform import transform_data
from validation import validate_data
from load import load_data


def main():

    print("===================================")
    print("Hospital Patient Care ETL Pipeline")
    print("===================================")


    # STEP 1: Extract

    print("\nSTEP 1: EXTRACT")

    (
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations
    ) = extract_data()


    # STEP 2: Transform

    print("\nSTEP 2: TRANSFORM")

    (
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations,
        risk_summary
    ) = transform_data(
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations
    )


    # STEP 3: Validate

    print("\nSTEP 3: VALIDATE")

    validate_data(
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations,
        risk_summary
    )


    # STEP 4: Load

    print("\nSTEP 4: LOAD")

    load_data(
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations,
        risk_summary
    )


    print("\n===================================")
    print("ETL PIPELINE COMPLETED SUCCESSFULLY")
    print("===================================")


if __name__ == "__main__":
    main()



## Step 5: ETL Pipeline Orchestration

# The `pipeline.py` file orchestrates the complete data engineering workflow.

# The pipeline executes four major stages in sequence:

#1. **Extract** – Reads hospital data from multiple CSV source systems.
#2. **Transform** – Cleans, standardizes, and combines the data.
#3. **Validate** – Checks data quality and ensures that business rules are satisfied.
#4. **Load** – Stores the validated data in MySQL.

# The pipeline ensures that each stage is completed before moving to the next stage.

# This provides a simple and repeatable automated workflow for hospital patient care analytics.