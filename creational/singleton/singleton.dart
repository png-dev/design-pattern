class Singleton {
    static Singleton _instance;

    static Singleton get instance => _instance ?? Singleton._();

    Singleton._() => _instance = this;
}