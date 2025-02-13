# import os
# import re
# import datetime

# def rename_quran_files(directory, log_file):
#     """
#     Rename Quran interpretation files to start with 'تفسير القرآن' followed by 
#     the date, ayat number, and surah name.

#     Args:
#         directory (str): The path to the directory containing the files to rename.
#     """
#     try:
#         with open(log_file, "a", encoding="utf-8") as log:
#             print(f"date of excute: { datetime.datetime.now()}\n")
#             log.write(f"date of excute: {datetime.datetime.now()}\n")
#             # List all files in the directory
#             files = os.listdir(directory)
#             for root, dirs, files in os.walk(directory):
#                 # Rename directories
#                     for dir_name in dirs:
#                         old_dir_path = os.path.join(root, dir_name)
#                         new_dir_name = re.sub(r"درس سماحة الشيخ الجمعة", "درس الجمعة", dir_name)
#                         new_dir_path = os.path.join(root, new_dir_name)
#                         if os.path.isdir(new_dir_path):
#                             continue
                        
#                         os.rename(old_dir_path, new_dir_path)
#                         log.write(f"Renamed directory: {old_dir_path} -> {new_dir_path}\n")
#                         print(f"Renamed directory: {old_dir_path} -> {new_dir_path}")
                # for file_name in files:
                    # old_path = os.path.join(root, file_name)
                    # log.write(f"Renamed: {old_path}")
                    # # Skip if it's not a file
                    # if not os.path.isfile(old_path):
                    #     continue

                    # Match the current file naming pattern
                    # Match the current file naming pattern
                    # match = re.match(r"(.+)\s\((\d+-\d+)\)\s(\d+)", file_name)
                    # match = re.match(r"(.+)\s(\w+)", file_name)
                    # new_name = re.sub(r"درس سماحة الشيخ الجمعة", "درس الجمعة", file_name)
                    # print(new_name)
                    # new_path = os.path.join(root, new_name)
                    # if os.path.isfile(new_path):
                    #     continue
                    
                    # # Rename the file
                    # os.rename(old_path, new_path)
                    # log.write(f"Renamed: {old_path} -> {new_path}\n")
                    # print(f"Renamed: {old_path} -> {new_path}")
                    # if match:
                    #     # surah_name = match.group(1).strip()
                    #     # ayat_number = match.group(2).strip()
                    #     # date = match.group(3).strip()
                    #     # surah_name = match.group(1).strip()
                    #     # print(surah_name)
                    #     # date = match.group(2).strip()
                    #     new_surah = "درس الجمعة"
                    #     if surah_name == "درس سماحة الشيخ الجمعة":
                    #         # Create the new file name
                    #         new_name = f"{new_surah} {date} {os.path.splitext(file_name)[1]}"
                    #         new_path = os.path.join(root, new_name)
                    #         if os.path.isfile(new_path):
                    #             continue
                            
                    #         # Rename the file
                    #         os.rename(old_path, new_path)
                    #         log.write(f"Renamed: {old_path} -> {new_path}\n")
                    #         print(f"Renamed: {old_path} -> {new_path}")
                    # else:
                    #     log.write(f"pattern_error: {old_path}\n")
                    #     print(f"error: {old_path}\n")
        
#     except Exception as e:
#         with open(log_file, "a", encoding="utf-8") as log:
#             log.write(f"Error: {e}")
#             print(f"Error: {e}")

# # Example usage:
# # Replace the directory path with the path to your files
# rename_quran_files('\\\\192.168.1.200\\Editing\\دروس التفسير', r'//192.168.1.200/Editing/دروس التفسير/rename_log.txt')






# ================================================================================
# move date to the first
import os
import re
import datetime

def convert_date(date_str):
    if len(date_str) != 8:
        return "Invalid date format"
    
    try:
        # Check if it's in yyyymmdd format (valid year range)
        year = int(date_str[:4])
        if 1900 <= year <= 2100:
            date_obj = datetime.datetime.strptime(date_str, "%Y%m%d")
        else:
            # Otherwise, interpret as ddmmyyyy
            date_obj = datetime.datetime.strptime(date_str, "%d%m%Y")
    except ValueError:
        return "Invalid date format"

    # Convert to yyyymmdd format
    return date_obj.strftime("%Y%m%d")

def rename_quran_files(directory, log_file):
    """
    Rename Quran interpretation files to start with 'تفسير القرآن' followed by 
    the date, ayat number, and surah name.

    Args:
        directory (str): The path to the directory containing the files to rename.
    """
    try:
        with open(log_file, "a", encoding="utf-8") as log:
            print(f"date of excute: { datetime.datetime.now()}\n")
            log.write(f"date of excute: {datetime.datetime.now()}\n")
            # List all files in the directory
            files = os.listdir(directory)
            for root, dirs, files in os.walk(directory):
                for file_name in files:
                    old_path = os.path.join(root, file_name)
                    log.write(f"Renamed: {old_path}")
                    # Skip if it's not a file
                    if not os.path.isfile(old_path):
                        continue
                    match = re.match(r".*?(\d{6}).*", file_name)
                    extention = file_name   
                    if match:
                        # surah_name = match.group(1).strip()
                        # ayat_number = match.group(2).strip()
                        date = match.group(1).strip()
                        date1 = convert_date(date)
                        
                        file_name = re.sub(date, "", file_name)
                        file_name = re.sub(r"\s{2}", "", file_name)
                        

                        new_name = f"{date1} {file_name}"
                        new_path = os.path.join(directory, new_name)
                        if os.path.isfile(new_path):
                            continue
                            
                        # Rename the file
                        os.rename(old_path, new_path)
                        log.write(f"Renamed: {old_path} -> {new_path}\n")
                        print(f"Renamed: {old_path} -> {new_path}")
                    else:
                        log.write(f"pattern_error: {old_path}\n")
                        print(f"error: {old_path}\n")
        
    except Exception as e:
        with open(log_file, "a", encoding="utf-8") as log:
            log.write(f"Error: {e}")
            print(f"Error: {e}")

# Example usage:
# Replace the directory path with the path to your files
rename_quran_files('\\\\192.168.1.200\\Editing\\دروس التفسير', r'//192.168.1.200/Editing/دروس التفسير/rename_log.txt')
# ================================================================================









# =====================================================================
# deleting empty folder
# import os
# import re
# import datetime

# def is_hidden(file_or_dir):
#     """Check if a file or directory is hidden."""
#     return file_or_dir.startswith('.') or file_or_dir.lower() == "thumbs.db"

# def delete_hidden_files(dir_path):
#     """Delete all hidden files in the directory."""
#     for item in os.listdir(dir_path):
#         item_path = os.path.join(dir_path, item)
#         if os.path.isfile(item_path) and is_hidden(item):
#             print(f"Deleting hidden file: {item_path}")
#             os.remove(item_path)

# def is_effectively_empty(dir_path):
#     """Check if a directory is empty or contains only hidden files."""
#     delete_hidden_files(dir_path)  # Remove hidden files first
#     for item in os.listdir(dir_path):
#         if not is_hidden(item):  # Ignore hidden files
#             return False  # Found a visible file or directory
#     return True

# def rename_quran_files(directory, log_file):
#     """
#     Rename Quran interpretation files to start with 'تفسير القرآن' followed by 
#     the date, ayat number, and surah name.

#     Args:
#         directory (str): The path to the directory containing the files to rename.
#     """
#     try:
#         with open(log_file, "a", encoding="utf-8") as log:
#             print(f"date of excute: { datetime.datetime.now()}\n")
#             log.write(f"date of excute: {datetime.datetime.now()}\n")
#             # List all files in the directory
#             files = os.listdir(directory)
#             for root, dirs, files in os.walk(directory, topdown=False):
#                 # Iterate through subdirectories in reverse order (bottom-up)
#                 for dir_name in dirs:
#                     dir_path = os.path.join(root, dir_name)

#                     # Check if the directory is effectively empty
#                     if is_effectively_empty(dir_path):
#                         print(f"Deleting directory: {dir_path}")
#                         os.rmdir(dir_path)  # Remove the directory
#                     else:
#                         print(f"keeping directory: {dir_path}")     
#     except Exception as e:
#         with open(log_file, "a", encoding="utf-8") as log:
#             log.write(f"Error: {e}")
#             print(f"Error: {e}")

# # Example usage:
# # Replace the directory path with the path to your files
# rename_quran_files('\\\\192.168.1.200\\Editing\\دروس التفسير', r'//192.168.1.200/Editing/دروس التفسير/rename_log.txt')
# ==================================================================




# ================================================================================
#move date to the first
# import os
# import re
# import datetime

# def convert_date(date_str):
#     if len(date_str) != 8:
#         return "Invalid date format"
    
#     try:
#         # Check if it's in yyyymmdd format (valid year range)
#         year = int(date_str[:4])
#         if 1900 <= year <= 2100:
#             date_obj = datetime.datetime.strptime(date_str, "%Y%m%d")
#         else:
#             # Otherwise, interpret as ddmmyyyy
#             date_obj = datetime.datetime.strptime(date_str, "%d%m%Y")
#     except ValueError:
#         return "Invalid date format"

#     # Convert to yyyymmdd format
#     return date_obj.strftime("%Y%m%d")

# def rename_quran_files(directory, log_file):
#     """
#     Rename Quran interpretation files to start with 'تفسير القرآن' followed by 
#     the date, ayat number, and surah name.

#     Args:
#         directory (str): The path to the directory containing the files to rename.
#     """
#     try:
#         with open(log_file, "a", encoding="utf-8") as log:
#             print(f"date of excute: { datetime.datetime.now()}\n")
#             log.write(f"date of excute: {datetime.datetime.now()}\n")
#             # List all files in the directory
#             files = os.listdir(directory)
#             for root, dirs, files in os.walk(directory):
#                 for file_name in files:
#                     old_path = os.path.join(root, file_name)
#                     log.write(f"Renamed: {old_path}")
#                     # Skip if it's not a file
#                     if not os.path.isfile(old_path):
#                         continue
#                     match = re.match(r"(\d+)-(\d+)-(\d+).*", file_name)
#                     extention = file_name
#                     if match:
#                         first_number = int(match.group(1).strip())
#                         if first_number < 10:
#                             first_number = "0" + str(first_number)
#                         sec_number = int(match.group(2).strip())
#                         if sec_number < 10:
#                             sec_number = "0" + str(sec_number)

#                         th_number = match.group(3).strip()
#                         # date1 = convert_date(date)
#                         new_name = f"{th_number}{sec_number}{first_number}{os.path.splitext(file_name)[1]}"
#                         print(new_name)
#                         # file_name = re.sub(date, "", file_name)
#                         # file_name = re.sub(r"\s{2}", "", file_name)
                        

#                         # new_name = f"{date1} {file_name}"
#                         new_path = os.path.join(directory, new_name)
#                         if os.path.isfile(new_path):
#                             continue
                            
#                         # Rename the file
#                         os.rename(old_path, new_path)
#                         log.write(f"Renamed: {old_path} -> {new_path}\n")
#                         print(f"Renamed: {old_path} -> {new_path}")
#                     else:
#                         log.write(f"pattern_error: {old_path}\n")
#                         print(f"error: {old_path}\n")
        
#     except Exception as e:
#         with open(log_file, "a", encoding="utf-8") as log:
#             log.write(f"Error: {e}")
#             print(f"Error: {e}")

# # Example usage:
# # Replace the directory path with the path to your files
# rename_quran_files('\\\\192.168.1.200\\Editing\\دروس التفسير\\111', r'//192.168.1.200/Editing/دروس التفسير/rename_log.txt')
# ================================================================================