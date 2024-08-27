from wtforms import (
    validators,
    StringField,
    DateField,
    EmailField,
    SelectField,
    TelField,
    Form,
)


class JobApplicationForm(Form):
    first_name = StringField(
        "first_name",
        [validators.Length(min=1, max=25), validators.InputRequired()],
    )
    last_name = StringField(
        "last_name", [validators.Length(min=1, max=25), validators.InputRequired()]
    )
    email = EmailField("email", [validators.Email(), validators.InputRequired()])
    phone = TelField(
        "phone",
        [validators.InputRequired(), validators.length(min=6, max=9)],
    )
    country = SelectField(
        "country",
        validators=[validators.InputRequired()],
        choices=[
            ("US", "United States"),
            ("UK", "United Kingdom"),
            ("CA", "Canada"),
            ("AU", "Australia"),
        ],
    )
    start_date = DateField("start_date", [validators.InputRequired()])
