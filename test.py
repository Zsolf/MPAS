import DPAA_BF
import DPAA_FF
import DPAA_WF
import Simple_FF
import Simple_BF
import Simple_WF

tests = ["BPP_50_50_0.1_0.8_0.txt", "BPP_50_500_0.2_0.7_2.txt", "BPP_100_100_0.1_0.7_6.txt", "BPP_100_1000_0.1_0.7_8.txt", 
         "BPP_200_200_0.2_0.7_0.txt", "BPP_400_750_0.2_0.8_6.txt", "BPP_500_125_0.2_0.8_7.txt", "BPP_500_500_0.2_0.8_8.txt",
          "BPP_750_120_0.2_0.8_6.txt", "BPP_1000_1000_0.1_0.7_0.txt", "BPP_1000_1000_0.2_0.7_6.txt"]

#tests = ["test.txt"]

for i in range(0,len(tests)):
    avg_density = 0
    density_list = []
    avg_time = 0
    avg_bins = 8
    bins_list = []
    for j in range(0,10):
        res = DPAA_WF.main(tests[i]) #change the algorithm here
        avg_density+= res[0]
        density_list.append(res[0])
        avg_time+= res[1]
        avg_bins+= res[2]
        bins_list.append(res[2])
    
    avg_density = avg_density/10
    avg_bins = avg_bins/10
    avg_time = avg_time/10
    min_density = str(min(density_list))
    max_density = str(max(density_list))
    min_bin = str(min(bins_list))
    max_bin = str(max(bins_list))

    print( tests[i] + "                              " +  "Density: " + str(avg_density) + "          "  + "Bins: " + str(avg_bins) )
    print(" Minimum density: " + min_density + "                "  +  "       "  + "Maximum Density: " + max_density + "      "  + " Minimum bin: " + min_bin + "         " + "Maximum bin: " + max_bin)
    print("Time: " + str(avg_time) + " seconds")
    print("------------------------------------------------------------------")

