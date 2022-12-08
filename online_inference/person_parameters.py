from fastapi import HTTPException
from pydantic import BaseModel, validator


def _check_category_value(field_name, field_value, possible_values):
    if field_value not in possible_values:
        raise HTTPException(status_code=400, detail=f'{field_name}={field_value} is incorrect value')


class PersonParameters(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

    @validator('sex')
    def check_sex(cls, value):
        _check_category_value('sex', value, [0, 1])
        return value

    @validator('cp')
    def check_cp(cls, value):
        _check_category_value('cp', value, [0, 1, 2, 3])
        return value

    @validator('fbs')
    def check_fbs(cls, value):
        _check_category_value('fbs', value, [0, 1])
        return value

    @validator('restecg')
    def check_restecg(cls, value):
        _check_category_value('restecg', value, [0, 1, 2])
        return value

    @validator('exang')
    def check_exang(cls, value):
        _check_category_value('exang', value, [0, 1])
        return value

    @validator('slope')
    def check_slope(cls, value):
        _check_category_value('slope', value, [0, 1, 2])
        return value

    @validator('ca')
    def check_ca(cls, value):
        _check_category_value('ca', value, [0, 1, 2, 3])
        return value

    @validator('thal')
    def check_thal(cls, value):
        _check_category_value('thal', value, [0, 1, 2])
        return value
