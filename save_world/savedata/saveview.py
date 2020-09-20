"""
The controller which has the route details for our app
"""
from dataclasses import dataclass

from flask import Blueprint, current_app, jsonify, render_template, request
from flask.views import MethodView

from savedata.model import UserSave


@dataclass
class SaveView(MethodView):
    """
    This has the routes for app to handle GET, PUT and POST requests.
    """
    def post(self):
        """
        Create new entry
        """
        if not request.is_json:
            return jsonify({"message": "Missing JSON in request"}), 400
        data = request.json

        if data.get('key', None) != current_app.config['SAVE_DATA_API_KEY']:
            return "Can not save", 401

        when_saved = data.get("dtime")
        how_saved = data.get("howsaved")
        thanks_to_people = data.get("thanks_to_people")

        try:
            user_save = UserSave(when_saved=when_saved,
                                 how_saved=how_saved, thanks=thanks_to_people)

            current_app.db.session.add(user_save)
            current_app.db.session.commit()
            return "Data saved", 201
        except Exception as e_x:
            return f"{e_x}", 401

    def put(self):
        """
        Update the entry
        """
        data = request.json

        if data.get('key', None) != current_app.config['SAVE_DATA_API_KEY']:
            return "Can not save", 401
        howsaved = data.get("howsaved")
        thanks_to_people = data.get("thanks_to_people")

        try:
            user_data = UserSave.query.filter_by(how_saved=howsaved).first()
            user_data.thanks = thanks_to_people
            current_app.db.session.commit()
            return jsonify(["Data updated"]), 201
        except Exception as e_x:
            return f"{e_x}", 401

    def get(self):
        """
        Get the data from the db
        """
        try:
            total_user_per_page = 3
            page_start = request.args.get('page', default=1, type=int)
            users_save = UserSave.query.paginate(page_start, total_user_per_page, False)
            return render_template("tables.html", users=users_save.items)

        except Exception as e_x:
            return f"{e_x}", 401


class IndexView(MethodView):
    """
    The root view for the app
    """
    def get(self):
        """
        Get the root view for our app.
        """
        return render_template("index.html")


save_api = Blueprint("save_world_view", __name__)
save_api_view = SaveView.as_view("save_api_view")

index_api = Blueprint("index_view", __name__)
index_api_view = IndexView.as_view("index_api_view")

save_api.add_url_rule("/save/world/",
                      view_func=save_api_view, methods=["POST", ])
save_api.add_url_rule("/save/world/",
                      view_func=save_api_view, methods=["PUT", ])
save_api.add_url_rule("/save/world/",
                      view_func=save_api_view, methods=["GET", ])
save_api.add_url_rule("/save/world/<int:page>/",
                      view_func=save_api_view, methods=["GET", ])

index_api.add_url_rule("/", view_func=index_api_view, methods=["GET", ])
