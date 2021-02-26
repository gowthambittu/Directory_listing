# Directory_listing
Directory listing using python optparse and OS module rather like dir in windows and ls in unix.


 >>python ls.py  -h

              Usage: ls.py [Options] [path1 [path2[path3]...pathN]]

                   The path is optional; if no path is given . will be taken

              Options:
                -h, --help            show this help message and exit
                -H, --hidden          show hidden files [default:off]
                -m, --modified        show last modified date/time [default:off]
                -o ORDER, --order=ORDER
                                      order by 'name','n','modified','m','size','s'
                                      [default:name]
                -r, --recursive       show recursive directories list [default:off]
                -s, --sizes           show sizes of the files [default:off]
  
  **Example**
  >>python ls.py -ms -os c:/
  >>

                  2020-02-29 13:39:35               0c:/$WINRE_BACKUP_PARTITION.MARKER
                  2021-02-21 15:19:31      16,777,216c:/swapfile.sys
                  2021-02-26 13:25:17   6,824,460,288c:/hiberfil.sys
                  2021-02-21 15:19:31   8,589,934,592c:/pagefile.sys
                                                     c:/$Recycle.Bin/
                                                     c:/Documents and Settings/
                                                     c:/Exercism/
                                                     c:/Intel/
                                                     c:/PanoptoRecorder/
                                                     c:/PerfLogs/
                                                     c:/Program Files/
                                                     c:/Program Files (x86)/
                                                     c:/ProgramData/
                                                     c:/Recovery/
                                                     c:/System Volume Information/
                                                     c:/Users/
                                                     c:/Windows/
                                                     c:/cygwin64/
                  4 files 14 directories



