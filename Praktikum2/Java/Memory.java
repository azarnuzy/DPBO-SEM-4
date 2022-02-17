class Memory extends Hardware {
    private String frequency;
    private int memorySize;
    private String supportsCuda;

    Memory() {
    }

    public void setFrequency(String frequency) {
        this.frequency = frequency;
    }

    public String getFrequency() {
        return this.frequency;
    }

    public void setMemorySize(int memorySize) {
        this.memorySize = memorySize;
    }

    public int getMemorySize() {
        return this.memorySize;
    }

    public void setSupportsCuda(String supportsCuda) {
        this.supportsCuda = supportsCuda;
    }

    public String getSupportsCuda() {
        return this.supportsCuda;
    }

    public void printMemory() {
        System.out.println("Frequency : " + getFrequency());
        System.out.println("Memory Size : " + getMemorySize());
        System.out.println("Support Cuda : " + getSupportsCuda());
    }
}
