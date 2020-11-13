class Student {
    String name;
    int age;

    Student(this.name, this.age);

    Student.fromSource(Student student) {
        name = student.name;
        age = student.age;
    }

    @Override
    Student clone() {
        return Student.fromSource(this);
    }
}

void main() {
    var student1 = Student('PNG', 10);
    var student2 = student1.clone();
    print(student1);
    print(student2);
}
