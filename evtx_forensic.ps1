
param (
    [string]$infile = $null
)

if (!$infile) {
    Write-Host "usage: evtx_forensic.ps1 -infile <evtx file in>"
    exit
}
$initem = Get-Item $infile
$outfile=$($initem.BaseName + ".txt")
$myJSON = [System.Text.StringBuilder]""
echo "Reading in the .evtx."
$events = get-winevent -path $infile 
echo "Converting to JSON"

$null = $myJSON.Append((ConvertTo-Json -InputObject $events)+",")

#foreach ($event in $events){
    #$null = $myJSON.Append((ConvertTo-Json -InputObject $event)+",")
#}
echo "finnished"
$x = $myJSON.ToString()
"["+$x.Substring(0,$x.Length-1)+"]" | Out-File -encoding ASCII -FilePath $outfile
python combinetxtlogs.py $outfile $initem.BaseName