$times = [int32](Read-Host -Prompt 'Enter number') - 1
$hash = [ordered]@{}
0..$times | % { $hash += @{"col$_" = 0} }

Write-Host "Ctrl-C to stop"

try
{
    while ($true){
        $sum = 0
        0..$times | % { $sum += Get-Random 2 }
        $hash["col$sum"] += 1
    }
}

finally
{
    ForEach($key in $hash.keys){
        Write-Host $hash[$key]
    }
    pause
}
