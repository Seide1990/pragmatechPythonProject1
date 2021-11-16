from django.core.exceptions import ValidationError
def mail_validator(mail):
    if not mail.endswith('gmail.com'):
        raise ValidationError('mail duzgun daxil edilmeyib')
    return True



    

