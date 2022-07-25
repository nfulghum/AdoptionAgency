from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Length, NumberRange, URL, Optional


class AddPetForm(FlaskForm):
    """Add pets form"""

    name = StringField("Pet Name", validators=[InputRequired()])
    species = SelectField("Species", choices=[
                          ("cat", "Cat"), ("dog", "Dog"), ("fish", "Fish")])
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[
                       Optional(), NumberRange(min=0, max=10)])
    notes = TextAreaField("Comments", validators=[Optional(), Length(min=5)])


class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField(
        "Photo URL",
        validators=[Optional(), URL()],
    )

    notes = TextAreaField(
        "Comments",
        validators=[Optional(), Length(min=10)],
    )

    available = BooleanField("Available?")
