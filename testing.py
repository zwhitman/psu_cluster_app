__author__ = 'zwhitman'

fullpath_tmp_state_folder = "C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb"
inputfile = "C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\\Alabama_22c8be8b_4979_402c_9d69_95444866a567.shp"
name3 = "C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\\Alabama_22c8be8b_4979_402c_9_standalone25.shp"
pdf_output = fullpath_tmp_state_folder+"\\pdf_test2.pdf"


fullpath_tmp_state_folder2 = '"'+fullpath_tmp_state_folder+'"'
fullpath_tmp_state_folder2 = fullpath_tmp_state_folder2.replace("\\", "\\\\")
inputfile2 = '"' + inputfile + '"'
inputfile2 = inputfile2.replace("\\","\\\\")
name4 = '"' + name3 + '"'
name4 = name4.replace("\\","\\\\")

pdf_output2 = '"' + pdf_output + '"'
pdf_output2 = pdf_output2.replace("\\","\\\\")

write_file = ['import arcpy','arcpy.env.workspace = ' + fullpath_tmp_state_folder2, 'arcpy.GroupingAnalysis_stats(' + inputfile2 +
             ', "COUNTYFP_1", ' + name4 +
             ', "2", "ALANDSQM", "CONTIGUITY_EDGES_CORNERS", "EUCLIDEAN", "0", "", "FIND_SEED_LOCATIONS", "", ' + pdf_output2 +', "DO_NOT_EVALUATE")']

# Open the file for writing
dataFile = open(fullpath_tmp_state_folder+'\\group_analysis.py', 'w')

print fullpath_tmp_state_folder
print fullpath_tmp_state_folder2
print name3
print name4
print pdf_output2
# Loop through each item in the list
# and write it to the output file.
for eachitem in write_file:
    dataFile.write(str(eachitem)+'\n')

# Close the output file
dataFile.close()

# import arcpy
# arcpy.GroupingAnalysis_stats("C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb", "COUNTYFP_1", "C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\\Alabama_22c8be8b_4979_402c_9_standalone22.shp", "2", "ALANDSQM", "CONTIGUITY_EDGES_CORNERS", "EUCLIDEAN", "0", "", "FIND_SEED_LOCATIONS", "", "C:\\Users\\zwhitman\\Documents\\census\\psu_app\\test_run\\tmp\\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\\pdf_test.pdf", "DO_NOT_EVALUATE")

# import arcpy
# arcpy.GroupingAnalysis_stats("C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb", "COUNTYFP_1", "C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\Alabama_22c8be8b_4979_402c_9_standalone22.shp", "2", "ALANDSQM", "CONTIGUITY_EDGES_CORNERS", "EUCLIDEAN", "0", "", "FIND_SEED_LOCATIONS", "", "C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\pdf_test.pdf", "DO_NOT_EVALUATE")



# import arcpy
# arcpy.GroupingAnalysis_stats("C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb", "COUNTYFP_1", "C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\Alabama_22c8be8b_4979_402c_9_standalone22.shp", "2", "ALANDSQM", "CONTIGUITY_EDGES_CORNERS", "EUCLIDEAN", "0", "", "FIND_SEED_LOCATIONS", "", GroupingOutput2_pdf, "DO_NOT_EVALUATE")

# import arcpy
# arcpy.GroupingAnalysis_stats("C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\", "COUNTYFP_1", "C:\Users\zwhitman\Documents\census\psu_app\test_run\tmp\Alabama_713c74b2_5250_4454_99f8_8a320b351ecb\Alabama_22c8be8b_4979_402c_9_standalone22.shp", "2", "ALANDSQM", "CONTIGUITY_EDGES_CORNERS", "EUCLIDEAN", "0", "", "FIND_SEED_LOCATIONS", "", GroupingOutput2_pdf, "DO_NOT_EVALUATE")

