import pandas as pd
from sqlalchemy import Date


def transform_data(
    patients,
    appointments,
    lab_reports,
    wearable,
    consultations
):

    # -----------------------------
    # Patients
    # -----------------------------

    patients = patients.drop_duplicates()

    patients["registration_date"] = pd.to_datetime(
        patients["registration_date"]
    )

    patients["age"] = pd.to_numeric(
        patients["age"],
        errors="coerce"
    )

    patients["age"] = patients["age"].fillna(
        patients["age"].median()
    )


    # -----------------------------
    # Appointments
    # -----------------------------

    appointments = appointments.drop_duplicates()

    appointments["appointment_date"] = pd.to_datetime(
        appointments["appointment_date"]
    )

    appointments["waiting_time_minutes"] = pd.to_numeric(
        appointments["waiting_time_minutes"],
        errors="coerce"
    )

    appointments["waiting_time_minutes"] = (
        appointments["waiting_time_minutes"].fillna(
            appointments["waiting_time_minutes"].median()
        )
    )


    # -----------------------------
    # Laboratory Reports
    # -----------------------------

    lab_reports = lab_reports.drop_duplicates()

    lab_reports["test_date"] = pd.to_datetime(
        lab_reports["test_date"]
    )

    lab_reports["result_value"] = pd.to_numeric(
        lab_reports["result_value"],
        errors="coerce"
    )

    lab_reports["result_value"] = lab_reports[
        "result_value"
    ].fillna(
        lab_reports["result_value"].median()
    )


    # -----------------------------
    # Wearable Data
    # -----------------------------

    wearable = wearable.drop_duplicates()

    wearable["reading_date"] = pd.to_datetime(
        wearable["reading_date"]
    )

    numeric_columns = [
        "heart_rate_bpm",
        "spo2_percent",
        "steps",
        "sleep_hours",
        "temperature_c"
    ]

    for column in numeric_columns:

        wearable[column] = pd.to_numeric(
            wearable[column],
            errors="coerce"
        )

        wearable[column] = wearable[column].fillna(
            wearable[column].median()
        )


    # -----------------------------
    # Doctor Consultations
    # -----------------------------

    consultations = consultations.drop_duplicates()

    consultations["consultation_date"] = pd.to_datetime(
        consultations["consultation_date"]
    )


    # -----------------------------
    # Create Patient Risk Summary
    # -----------------------------

    high_risk = consultations[
        consultations["risk_level"] == "High"
    ]

    high_risk_count = (
        high_risk.groupby("patient_id")
        .size()
        .reset_index(name="high_risk_consultations")
    )

    abnormal_labs = lab_reports[
        lab_reports["abnormal_flag"] != "Normal"
    ]

    abnormal_lab_count = (
        abnormal_labs.groupby("patient_id")
        .size()
        .reset_index(name="abnormal_lab_count")
    )

    wearable_risk = wearable[
        (wearable["heart_rate_bpm"] > 100) |
        (wearable["spo2_percent"] < 94)
    ]

    wearable_risk_count = (
        wearable_risk.groupby("patient_id")
        .size()
        .reset_index(name="abnormal_wearable_readings")
    )


    # Combine risk indicators

    risk_summary = patients[
        ["patient_id", "age", "gender", "city"]
    ].copy()

    risk_summary = risk_summary.merge(
        high_risk_count,
        on="patient_id",
        how="left"
    )

    risk_summary = risk_summary.merge(
        abnormal_lab_count,
        on="patient_id",
        how="left"
    )

    risk_summary = risk_summary.merge(
        wearable_risk_count,
        on="patient_id",
        how="left"
    )


    # Replace missing counts with zero

    risk_columns = [
        "high_risk_consultations",
        "abnormal_lab_count",
        "abnormal_wearable_readings"
    ]

    risk_summary[risk_columns] = (
        risk_summary[risk_columns]
        .fillna(0)
        .astype(int)
    )


    # Calculate risk score

    risk_summary["risk_score"] = (
        risk_summary["high_risk_consultations"] * 3
        + risk_summary["abnormal_lab_count"] * 2
        + risk_summary["abnormal_wearable_readings"]
    )


    # Assign final risk category

    def classify_risk(score):

        if score >= 8:
            return "High"

        elif score >= 4:
            return "Medium"

        else:
            return "Low"


    risk_summary["risk_category"] = (
        risk_summary["risk_score"]
        .apply(classify_risk)
    )


    print("Data transformation completed successfully.")

    return (
        patients,
        appointments,
        lab_reports,
        wearable,
        consultations,
        risk_summary
    )



## Step 2: Data Transformation

# The transformation stage prepares the extracted data for analysis and storage.

# The following transformations are performed:

#1. Duplicate records are removed.
#2. Date columns are converted into proper datetime format.
#3. Numeric columns are converted into numeric data types.
#4. Missing numeric values are replaced using the median.
#5. Abnormal laboratory results are identified.
#6. Abnormal wearable readings are identified.
#7. High-risk consultation records are identified.

# A patient risk summary is then created by combining information from patient registration, laboratory reports, wearable devices, and doctor consultations.

# A simple risk score is calculated:

# Risk Score = High-Risk Consultations × 3 + Abnormal Lab Results × 2+ Abnormal Wearable Readings

# The score is then classified into Low, Medium, or High risk.

# This stage represents the **Transform** phase of the ETL pipeline.