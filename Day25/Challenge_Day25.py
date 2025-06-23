from pydantic import BaseModel, EmailStr, validator, field_validator


class Details(BaseModel):
    name: str
    email_id: EmailStr
    age: int

    @field_validator("age")
    @classmethod
    def validate_age(cls, value):
        if value<18 or value>100:
            raise ValueError(f"The mentioned age is not within the range")
        return value

input_datas = Details(name="Suryapraksh", email_id="surya.hal.sp@gmail.com", age=17)
print(input_datas)