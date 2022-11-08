public interface Solution
{
    /** @return an integer value that ranges from 1 (very acidic)
    * to 14 */
    int getPH();
    /** Set PH to newValue.
    * @param newValue the new PH value */
    void setPH(int newValue);
}
