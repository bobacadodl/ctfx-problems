#this program decodes the full message, but due to precision errors,
#the flag was changed to being the first 11 characters.

s = "00011101010110111011111010110101010100101101011111100011000111000100010001001100110100001000011001110001111101101011110010010110110010111011000101111000011101000000111110011011000111111110101000001010011011000011001010000001110011101110101110111001001101011110111011001101100101111001111100001000010100001000000101111100111000110100001001111"
val = int(s,2)
 
print(val)
 
# Base 26 Weighted by frequency
prob = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.0236, 0.0015, 0.01974, 0.00074]
 
prefix = [0 for i in range(27)]
prefix[0] = 0.0
for i in range(1, 27):
    prefix[i] = prefix[i - 1] + prob[i - 1]
 
l = 80
ans = ""
delta = 2 ** len(s)
for i in range(l):
    tmp = [round(x*delta) for x in prefix]
    it = 0
    while it < 26 and tmp[it] < val:
        it += 1
    it -= 1
    ans += chr(it + 97)
    val -= tmp[it]
    delta = tmp[it+1] - tmp[it]
 
print(ans)