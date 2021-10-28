from datetime import datetime, timedelta
from re import match
from flask import jsonify, request, current_app
from app.models.certificate_model import Certificate
from app.exeptions.exeptions import (
    InvalidExpirationTime,
    InvalidUserName,
    InvalidKey,
    InvalidGroup,
)
from sqlalchemy.exc import DataError, IntegrityError, NoResultFound
from app.models.group_model import Group


def create_certificate():

    data = request.json

    try:

        valid_keys = ["username", "name", "description", "groups", "expiration"]
        invalid_keys = []
        for key in data.keys():
            if not key in valid_keys:
                invalid_keys.append(key)

        if invalid_keys:
            raise InvalidKey(
                {"avalible_keys": valid_keys, "wrong_keys_sended": invalid_keys}
            )

        expiration_time = data["expiration"]

        if expiration_time >= 10 and expiration_time <= 3650:

            data.setdefault(
                "expirated_at", datetime.now() + timedelta(days=data["expiration"])
            )
        else:
            raise InvalidExpirationTime

    except (InvalidExpirationTime, TypeError):
        return {"Msg": "Expiration date must be an integer between 10 and 3650"}, 400

    except InvalidKey as error:
        return jsonify({"Msg: Invalid key(s)": error.args}), 422

    try:
        username = data["username"]
        if not match("^[A-Za-z0-9_-]*$", username):
            raise InvalidUserName
        if not username:
            raise InvalidUserName

        groups_of_this_certificate = data.pop("groups")

        new_certificate = Certificate(**data)

        for group_of_this_certificate in groups_of_this_certificate:

            valid_groups = [1, 15, 30]
            group_model = Group.query.filter_by(type=group_of_this_certificate).first()

            if not group_model:
                raise InvalidGroup(
                    {
                        "valid_groups": valid_groups,
                        "invalid_group_sended": group_of_this_certificate,
                    }
                )

            new_certificate.groups.append(group_model)

        session = current_app.db.session

        session.add(new_certificate)
        session.commit()

    except (InvalidUserName, TypeError):
        return {"Msg": "Username must contain only a-z letters and integers"}, 400

    except KeyError as error:
        return jsonify(error.args)

    except DataError:
        return (
            {
                "Msg": "username must contain a maximum of 30 characters, and name a maximum of 255 characters"
            },
            400,
        )

    except InvalidKey as error:
        return jsonify({"Msg: Invalid key(s)": error.args}), 422

    except InvalidGroup as error:
        return jsonify({"Msg: Invalid group(s)": error.args}), 422

    except IntegrityError as error:
        error_message = error.args[0]

        if "null value" in error_message:
            return {"Msg": "fill in all required fields"}, 400

        if "duplicate key" in error_message:
            return {"msg": "Username already exists"}, 409

    return jsonify(new_certificate), 201


def list_all_certificates():

    certificates_list = Certificate.query.all()
    return jsonify(certificates_list), 200


def get_certificate_by_id(id: int):

    certificate = Certificate.query.get(id)

    return jsonify(certificate), 200


def update_certificate(certificate_id: int):

    try:
        data = request.json

        certificate = Certificate.query.filter_by(id=certificate_id).one()

        certificate.updated_at = datetime.now()

        groups_of_this_certificate = data.pop("groups")

        for group_of_this_certificate in groups_of_this_certificate:

            valid_groups = [1, 15, 30]
            group_model = Group.query.filter_by(type=group_of_this_certificate).first()

            if not group_model:
                raise InvalidGroup(
                    {
                        "valid_groups": valid_groups,
                        "invalid_group_sended": group_of_this_certificate,
                    }
                )

            certificate.groups.append(group_model)

        Certificate.query.filter_by(id=certificate_id).update(data)

        session = current_app.db.session
        session.add(certificate)
        session.commit()

        updated_certificate = Certificate.query.get(certificate_id)
    except NoResultFound:
        return {"msg": "certificate not found"}, 404
    return jsonify(updated_certificate), 200


def delete_certificate(id: int):
    certificate = Certificate.query.get_or_404(id)
    current_app.db.session.delete(certificate)
    current_app.db.session.commit()

    return jsonify(certificate), 200
