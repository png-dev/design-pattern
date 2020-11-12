class Singleton {
    private static instance: Singleton;

    private constructor() {
    }

    public class getInstance(): Singleton {
        if(!Singleton.instance) {
            Singleton.instance = new Singleton()
        }
        return Singleton.instance
    }
}

function test() {
    const s1 = Singleton.getInstance();
    const s2 = Singleton.getInstance();

    if(s1 === s2) {
        console.log('Singleton work')
    } else {
        console.log('Singleton Faild')
    }
}