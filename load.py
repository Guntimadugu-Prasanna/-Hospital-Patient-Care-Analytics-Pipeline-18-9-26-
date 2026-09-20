from sqlalchemy import create_engine
from config import DB_CONFIG


def load_data(
    patients,
    appointments,
    lab_reports,
    wearable,
    consultations,
    risk_summary
):

    connection_string = (
        f"mysql+mysqlconnector://"
        f"{DB_CONFIG['user']}:"
        f"{DB_CONFIG['password']}@"
        f"{DB_CONFIG['host']}/"
        f"{DB_CONFIG['database']}"
    )

    engine = create_engine(connection_string)


    # Load patient table

    patients.to_sql(
        "patients",
        con=engine,
        if_exists="replace",
        index=False
    )


    # Load appointments

    appointments.to_sql(
        "appointments",
        con=engine,
        if_exists="replace",
        index=False
    )


    # Load laboratory reports

    lab_reports.to_sql(
        "laboratory_reports",
        con=engine,
        if_exists="replace",
        index=False
    )


    # Load wearable readings

    wearable.to_sql(
        "wearable_readings",
        con=engine,
        if_exists="replace",
        index=False
    )


    # Load consultations

    consultations.to_sql(
        "consultations",
        con=engine,
        if_exists="replace",
        index=False
    )


    # Load risk summary

    risk_summary.to_sql(
        "patient_risk_summary",
        con=engine,
        if_exists="replace",
        index=False
    )


    print("All data loaded into MySQL successfully.")





## Step 4: Data Loading

# The loading stage stores the validated data in a MySQL database.

# SQLAlchemy is used to create a connection between Python and MySQL.

# The transformed DataFrames are stored as separate database tables:

# patients
# appointments
# laboratory_reports
# wearable_readings
# consultations
# patient_risk_summary

# The `to_sql()` function transfers the Pandas DataFrames into MySQL tables.

# The database acts as the central storage layer for the hospital analytics system.

# This represents the **Load** phase of the ETL pipeline.