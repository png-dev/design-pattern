class Prototype {
    public primitive: any;
    public component: object;

    public clone(): this {
        const clone = Object.clone(this);
        clone.component = Object.create(this.component);
        return clone;
    }
}

function clientCode() {
    const prototype = new Prototype()
    prototype.primitive = 245
    prototype.component = new Date()

    const prototypeClone = prototype.clone()
}