import datetime
import locale
locale.setlocale(locale.LC_ALL, "")
from optparse import OptionParser
import os
from symbol import del_stmt


def main():
    count = [0,0]
    opts, paths = process_options()
    if not opts.recursive:
        filenames = []
        dirnames = []
        for path in paths:
            if os.path.isfile(path):
                filenames.append(path)
                continue
            for name in os.listdir(path):
                if not opts.hidden and name.startswith("./"):
                    continue
                fullname = os.path.join(path,name)
                if fullname.startswith("./"):
                    fullname = fullname[2:]
                if os.path.isfile(fullname):
                    filenames.append(fullname)
                else:
                    dirnames.append(fullname)
        count[0] += len(filenames)
        count[1] += len(dirnames)
        process_lists(opts,filenames,dirnames)
    else:
        for path in paths:
            for root,dirs,files in os.walk(path):
                if not opts.hidden:
                    dirs[:] = [dir for dir in dirs if not dir.startswith("./")]
                filenames = []
                for name in files:
                    if not opts.hidden and name.startswith("./"):
                        continue
                    fullname = os.path.join(root,name)
                    if fullname.startswith("./"):
                        fullname = fullname[2:]
                    filenames.append(fullname)
                count[0] += len(filenames)
                count[1] += len(dirs)
                process_lists(opts,filenames,dirs)
    print("{0} file{1} {2} director{3}".format(
        "{0:n}".format(count[0]) if count[0] else "no",
        "s" if count[0] != 1 else "",
        "{0:n}".format(count[1]) if count[1] else "no",
        "ies" if count[1] != 1 else "y"
    ))




def process_lists(opts,filenames,dirnames):
    key_lines = []
    for name in filenames:
        modified = ""
        if opts.modified:
            try:
                modified = (datetime.datetime.fromtimestamp(
                    os.path.getmtime(name)).isoformat(" ")[:19]+" ")
            except EnvironmentError:
                modified = "{0:>19}".format("Unknown")
        size = ""
        if opts.sizes:
            try:
                size = "{0:>15n}".format(os.path.getsize(name))
            except EnvironmentError:
                size = "{0:>15}".format("unknown")
        if os.path.islink(name):
            name += "->" + os.path.realpath(name)
        if opts.order in {"m","modified"}:
            order_key = modified
        elif opts.order in {"s","size"}:
            order_key = size
        else:
            order_key = name
        key_lines.append((order_key,"{modified}{size}{name}".format(**locals())))
    size = "" if not opts.sizes else " "*15
    modified = "" if not opts.modified else " "*20
    for name in sorted(dirnames):
        key_lines.append((name, modified + size + name + "/"))
    for key,line in sorted(key_lines):
        print(line)




def process_options():
    usage = """Usage: %prog [Options] [path1 [path2[path3]...pathN]]
     
     The path is optional; if no path is given . will be taken"""
    parser = OptionParser(usage= usage)
    parser.add_option("-H","--hidden", dest = "hidden",
                      action= "store_true",
                      help = ("show hidden files [default:off]"))

    parser.add_option("-m","--modified", dest = "modified",
                       action = "store_true",
                       help = ("show last modified date/time [default:off]"))
    orderlist = ['name','n','modified',"m",'size','s']
    parser.add_option("-o","--order",dest = "order",
                       choices = orderlist,
                       help= ("order by {0} [default:name]".format(",".join((["'"+ x + "'" for x in orderlist])))))
    parser.add_option("-r","--recursive", dest = "recursive",
                       action = "store_true",
                       help = ("show recursive directories list [default:off]"))
    parser.add_option("-s","--sizes",dest = "sizes",
                      action ="store_true",
                      help=("show sizes of the files [default:off]"))
    parser.set_defaults(order = orderlist[0])
    opts,args = parser.parse_args()
    if not args:
        args = ["."]
    return opts,args

main()