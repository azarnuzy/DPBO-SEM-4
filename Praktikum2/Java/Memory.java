class Memory extends Hardware {
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
        System.out.println("Frequency : " + this.frequency);
        System.out.println("Memory Size : " + this.memorySize);
        System.out.println("Support Cuda : " + this.supportCuda);
    }
}
