def validate_data(
    patients,
    appointments,
    lab_reports,
    wearable,
    consultations,
    risk_summary
):

    print("\nStarting data validation...")

    # Check for null values

    assert patients.isnull().sum().sum() == 0, \
        "Patients contain null values"

    assert appointments.isnull().sum().sum() == 0, \
        "Appointments contain null values"

    assert lab_reports.isnull().sum().sum() == 0, \
        "Lab reports contain null values"

    assert wearable.isnull().sum().sum() == 0, \
        "Wearable data contains null values"

    assert consultations.isnull().sum().sum() == 0, \
        "Consultations contain null values"

    assert risk_summary.isnull().sum().sum() == 0, \
        "Risk summary contains null values"


    # Check duplicate patient IDs

    assert patients["patient_id"].is_unique, \
        "Duplicate patient IDs found"


    # Check valid age

    assert patients["age"].between(0, 120).all(), \
        "Invalid patient age found"


    # Check appointment waiting time

    assert (
        appointments["waiting_time_minutes"] >= 0
    ).all(), \
        "Invalid waiting time found"


    # Check risk categories

    valid_risk = ["Low", "Medium", "High"]

    assert risk_summary[
        "risk_category"
    ].isin(valid_risk).all(), \
        "Invalid risk category found"


    # Check patient IDs

    assert risk_summary[
        "patient_id"
    ].isin(patients["patient_id"]).all(), \
        "Invalid patient ID in risk summary"


    print("All validation checks passed successfully.")

    return True




## Step 3: Data Validation

# Data validation ensures that incorrect or incomplete data is not loaded into the hospital database.

# The validation process checks:

# Whether null values remain after transformation.
# Whether patient IDs are unique.
# Whether patient ages are within a valid range.
# Whether waiting times are non-negative.
# Whether risk categories contain only Low, Medium, or High.
# Whether patient IDs in the risk summary exist in the patient master data.

# Assertions are used to stop the pipeline if an important validation rule fails.

# This improves data quality and prevents unreliable data from reaching the database.
.............
