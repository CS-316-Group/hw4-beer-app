from wtforms import SelectField, SubmitField


class ServingsFormFactory:
	@staticmethod
	def form(beer_names):
		class F(@TODO):
		beer_sel = SelectField('Beer Name', choices= @TODO )
		submit = SubmitField('Submit')
		return F()