export default class HolbertonCourse{
    constructor(name = String, length = Number, students = Array){
        this.name = name
        this.length = length
        this.students = students
    }
    get name(){
        return this._name;
    }
    set name(value){
        if (typeof value !== "string"){
            throw new TypeError("String Error");
        }
        this._name = value;
    }
    get length(){
        return this._length;
    }
     set length(value){
        if (typeof value !== "number"){
            throw new TypeError("Length must be a number");
        }
        this._length = value;
    }
        get students(){
        return this._students;
    }
     set students(value){
        if (!Array.isArray(value) || !value.every((el) => typeof el === 'string')){
            throw new TypeError("Array Error");
        }
        this._students = value;
    }
}
