from flask import Flask,request,jsonify,Response,abort,make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask (__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://tododb_user:1237@localhost:5432/tododb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

api = Api(app)



class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String, nullable = False)
    
    def __repr__(self):
        return "<task(id='%d', task='%s')>" % (
                                self.id, self.task)


class TaskAPI(Resource):
    def get(self):
        ID ="id"
        task_ = "task"
        alltasks = Task.query.all()
        
        L_id=[]
        L_tasks=[]
        for everytask in alltasks :
            L_id.append(everytask.id)
            L_tasks.append(everytask.task)
        L_obj = []
        for i in range(len(L_id)):
            obj = {ID : L_id[i],task_:L_tasks[i]}
            L_obj.append(obj)

        return jsonify(L_obj)

    def post(self):
        task_to_do = request.get_json()
        createdtask = task_to_do["task"]
        newtask = Task(task=createdtask)
        db.session.add(newtask)
        db.session.commit()
        return make_response(jsonify({
            "message" : "Task added successfully."
        }),201)
        
        

class ParticularTaskAPI(Resource):
    def get(self,num):
        try :
            particulartask = Task.query.filter_by(id = num).first()
            return jsonify({
                "task": particulartask.task
                })
        except :
            return abort(404)

    def put(self,num):
        try:
            task_to_edit = request.get_json()
            newtask = task_to_edit['task']
            task = Task.query.filter_by(id=num).first()
            task.task = newtask
            db.session.commit()
            return {"message": "task updated successfully"}
        except:
            return abort(405)
        
    def delete(self,num):
        try :
            particulartask = Task.query.filter_by(id = num).first()
            db.session.delete(particulartask)
            db.session.commit()
            return jsonify({
            "message" : "Deleted task successfully" 
            })
        except :
            return abort(404)


api.add_resource(TaskAPI, '/task')
api.add_resource(ParticularTaskAPI, '/task/<int:num>')

if __name__ == '__main__':
    app.run(debug=True)
 