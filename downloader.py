import subprocess  
import os  
import imdb  

location = './dbfiles'  
imdb_script = './code/bin/imdbpy2sql.py'  
base_download_url = 'ftp://ftp.fu-berlin.de/pub/misc/movies/database/'  
to_download_files = [  
    'movie-links.list.gz', 'keywords.list.gz', 'directors.list.gz',  
    'editors.list.gz', 'genres.list.gz', 'language.list.gz',  
    'movies.list.gz', 'producers.list.gz', 'production-companies.list.gz', 'ratings.list.gz',  
    'writers.list.gz', 'countries.list.gz', 'complete-cast.list.gz']  

mysql_ip = 'localhost'  
mysql_user = 'root'  
mysql_passwd = 'zxasqw'  
mysql_db = 'imdb'  

def download_db_files():  
    for file in to_download_files:  
        if not os.path.isfile(location + '/' + file):  
            url = base_download_url + file  
            print 'Downloading ', url  
            args = 'wget' + ' -P '+ location + " " + url  
            # t_pro = subprocess.Popen(args)
            os.system(args)  
            # block model too slow  
            # t_pro.wait()  


def trans_db_to_local():  
    while True:  
        allDone = True  
        for file in to_download_files:  
            if not os.path.isfile(location + '/' + file):  
                #print 'need file: ', location+file  
                allDone = False  
                break  
        if allDone == True:  
            break  

    print 'Running imdbpy2sql.py begin'  
    # mysql://user:password@host/database  
    mysql_list = ['mysql://', mysql_user, ':', mysql_passwd, '@', mysql_ip, '/', mysql_db]  
    subprocess.call(imdb_script + ' -d ' + location + ' -u ' + ''.join(mysql_list) + ' --mysql-force-myisam', shell=True)  
    print 'Running imdbpy2sql.py. over'  


def run():  
    download_db_files()  
    trans_db_to_local()  

if __name__ == '__main__':  
    run()

