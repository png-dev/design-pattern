public class ComputerBuilder{
    private String HDD;
    private String  RAM;
    private boolean isBluetoothEnable;

    public ComputerBuilder(String hdd, String ram) {
        this.HDD = hdd;
        this.RAM = ram;
    }

    public ComputerBuilder setBluetoothEnable(boolean isBluetoothEnable) {
        this.isBluetoothEnable = isBluetoothEnable;
        return this;
    }

    public Computer build() {
        return new Computer(this);
    }
}

public class Computer{
    private String HDD;
    private String  RAM;
    private boolean isBluetoothEnable;

    private Computer(ComputerBuilder builder) {
        this.HDD = builder.HDD;
        this.RAM = builder.RAM;
        this.isBluetoothEnable = builder.isBluetoothEnable;

    }

}

public class BuilderPattern {
    public static void main(String[] args) {
        Computer computer = new new Computer.ComputerBuilder("500 GB", "2 GB").setBluetoothEnabled(true).build();
    }
}