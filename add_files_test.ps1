function New-Py-File {
    param (
        $Tld,
        $Fpath,
        $Fname
    )

    New-Item -Path .\$Tld\$Fpath -ItemType Directory
    New-Item -Path .\$Tld\$Fpath\$Fname -ItemType File
    
}

New-Py-File 06-two-heaps 02-find-medium find_medium.py
New-Py-File 06-two-heaps 03-sw-medium sw_medium.py
New-Py-File 06-two-heaps 04-schedule-tasks schedule_tasks.py