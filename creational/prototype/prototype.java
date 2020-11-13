public class Student implements Cloneable {
    private String name;
    private int age;

    public Student( String name, int age) {
        super();
        this.name = name
        this.age = age
    }

    @Override
    protected Student clone() {
         return (Student) super.clone()
    }
}

public class Main {
    public static void main(String [] args) {
        Student student1 = new Student('PNG', 10)

        Student student2 = student1.clone()

        System.out.println(student1)
        System.out.println(student2)
    }
}