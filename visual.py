import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

UPLOAD_FOLDER = 'visuals/uploads/'

def generate_daily(result,chart_type):
     x=[]
     y=[]
     for res in result:
            x.append(res[0])
            # print(res[0])
            # print(res[1])
            y.append(res[1])
     if chart_type=='bar':
           plt.bar(y,x)
     elif chart_type=='line':
           plt.plot(y,x,marker='o',color='orange')

     plt.xlabel('Date')
     plt.ylabel('Calorie count')
     plt.title(' Date vs Calorie count')
    #  plt.show()  
    #  C:\Users\Kushal jain\Desktop\Calorie Tracking app\frontend\static\uploads
     file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\daily.png'
     file_path2 = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\daily.pdf'

     if os.path.exists(file_path):
           os.remove(file_path)
     plt.savefig(file_path)

     if os.path.exists(file_path2):
           os.remove(file_path2)
     plt.savefig(file_path2)

     plt.clf()
    
def generate_weekly(result,chart_type):
     x=[]
     y=[]
     for res in result:
            x.append(res[0])
            # print(res[0])
            # print(res[1])
            y.append(res[1])
     if chart_type=='bar':
           plt.bar(y,x)
     elif chart_type=='line':
           plt.plot(y,x,marker='o',color='orange')
     plt.xlabel('Week')
     plt.ylabel('Calorie count')
     plt.title(' Weekly Calorie Count')
     file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\weekly.png'
     file_path2 = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\weekly.pdf'

     if os.path.exists(file_path):
           os.remove(file_path)
     plt.savefig(file_path)

     if os.path.exists(file_path2):
           os.remove(file_path2)
     plt.savefig(file_path2)
     plt.clf()

def generate_monthly(result,chart_type):
     x=[]
     y=[]
     for res in result:
            x.append(res[0])
            # print(res[0])
            # print(res[1])
            y.append(res[1])
     if chart_type=='bar':
           plt.bar(y,x)
     elif chart_type=='line':
           plt.plot(y,x,marker='o',color='orange')
     plt.xlabel('Month')
     plt.ylabel('Calorie count')
     plt.title(' Montly Calorie Count')
     file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\monthly.png'
     file_path2 = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\monthly.pdf'

     if os.path.exists(file_path):
           os.remove(file_path)
     plt.savefig(file_path)

     if os.path.exists(file_path2):
           os.remove(file_path2)
     plt.savefig(file_path2)

     plt.clf()

def generate_combined(result_daily, result_weekly, result_monthly, chart_type):
    x_daily = [res[0] for res in result_daily]
    y_daily = [res[1] for res in result_daily]

    x_weekly = [res[0] for res in result_weekly]
    y_weekly = [res[1] for res in result_weekly]

    x_monthly = [res[0] for res in result_monthly]
    y_monthly = [res[1] for res in result_monthly]

    fig, axs = plt.subplots(3, 1, figsize=(8, 12))

    if chart_type == 'bar':
        axs[0].bar(y_daily, x_daily)
        axs[1].bar(y_weekly, x_weekly)
        axs[2].bar(y_monthly, x_monthly)
    elif chart_type == 'line':
        axs[0].plot(y_daily, x_daily, marker='o', color='orange')
        axs[1].plot(y_weekly, x_weekly, marker='o', color='orange')
        axs[2].plot(y_monthly, x_monthly, marker='o', color='orange')

    axs[0].set_xlabel('Date')
    axs[0].set_ylabel('Calorie count')
    axs[0].set_title('Daily Count')

    axs[1].set_xlabel('Week')
    axs[1].set_ylabel('Calorie count')
    axs[1].set_title('Weekly Average')

    axs[2].set_xlabel('Month')
    axs[2].set_ylabel('Calorie count')
    axs[2].set_title('Monthly Average')
    
    plt.subplots_adjust(hspace=0.5)

    file_path = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\combined.png'
    file_path2 = 'C:\\Users\\Kushal jain\\Desktop\\Calorie Tracking app\\frontend\\static\\uploads\\combined.pdf'

    if os.path.exists(file_path):
        os.remove(file_path)
    plt.savefig(file_path)

    if os.path.exists(file_path2):
        os.remove(file_path2)
    plt.savefig(file_path2)

    plt.clf()