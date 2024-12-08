params.str = params.str ?: "Hello World"
params.outputDir = params.outputDir ?: './results'

workflow {
    inputString = Channel.from(params.str)

    inputString.view()

    exampleTask(inputString)
}

process exampleTask {
    input:
    val inputString

    output:
    path("${params.outputDir}/allcaps.txt")

    script:
    """
    mkdir -p ${params.outputDir}
    echo $inputString | tr '[a-z]' '[A-Z]' > ${params.outputDir}/allcaps.txt
    """
}
