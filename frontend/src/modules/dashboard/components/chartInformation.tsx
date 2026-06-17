interface ChartInformation {
    pergunta: string;
    dados: string;
    tipo: string;
}

const codeGraph = (typeGraph: string) => {
    switch (typeGraph) {
        case "grafico_barras_horizontal":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
    Plot.barX(dadosFormatados, {
        x: "valor",
        y: primeiraDim,
        fill: "steelblue",
    }),
    ],
    x: { grid: true },
    marginLeft: 120,
})`

        case "grafico_barras_vertical":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
    Plot.barY(dadosFormatados, {
        x: primeiraDim,
        y: "valor",
        fill: "steelblue",
    }),
    ],
    x: { tickRotate: -45 },
    marginBottom: 100,
})`

        case "graficos_linhas":
            return `
Plot.plot({
    width: 530,
    height: 530,
    marks: [
        Plot.line(dadosGraficoLinhasFormatados, { 
            // Agora 'x' usa a chave de texto (rótulo)
            x: chaveTexto, 
            y: "valor", 
            stroke: "steelblue"
        }),
        Plot.dot(dadosGraficoLinhasFormatados, { 
            x: chaveTexto, 
            y: "valor", 
            fill: "darkblue"
        }),
    ],
    x: { 
        domain: domainOrder, // Garante a ordem correta dos rótulos
        label: chaveTexto,
        tickRotate: -45,
        padding: 0.1 // Adiciona um pequeno espaço nas bordas
    },
    y: { 
        grid: true,
        label: "Valor"
    },
    marginBottom: 100 // Aumenta para acomodar os rótulos girados
})`

        case "mapas_coropleticos":
            return `
Plot.plot({
    width: 530,
    height: 530,
    axis: null,
    color: {
        type: "quantize",
        scheme: "blues",
        label: "Valor",
        legend: true,
    },
    marks: [
        Plot.geo(brasil, {
            fill: feature => {
            const estado = feature.properties.Estado;
            return dados.find(
                (d) => Object.values(d.dimensoes)[0] === estado
            )?.valor;
            },
            stroke: "lightgray",
        }),
    ],
})`

        case "graficos_com_proporcao":
            return `
Plot.plot({
    width: 530,
    height: 530,
    x: { label: primeiraDim, tickRotate: -40 },
    y: { label: "Valor" },
    color: { legend: true },
    marks: [
        Plot.barY(dadosFormatados, {
            x: primeiraDim,
            y: "valor",
            fill: terceiraDim || segundaDim || primeiraDim,
                      
        }),
    ],
    marginBottom: 120,
})`

        default:
            return `Tipo de gráfico incorreto.`
    }
}

function intermediateCode(tipo: string) {
    if(tipo === "mapas_coropleticos") {
            return (
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`brasil = (
    await fetch("https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/main/geojson/br_states.json")
    .then(res => res.json())
    .catch((error) => console.error("Erro ao carregar mapa:", error))
)`}
                </pre>
            )
    } else if(tipo === "graficos_linhas") {
        return (
            <>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">{`dims = dados[0].dimensoes`}</pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">{`chaveNumerica = Object.keys(dims).find(k => typeof dims[k] === "number");`}</pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">{`chaveTexto = Object.keys(dims).find(k => typeof dims[k] === "string");`}</pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`// 1. Ordena os dados pelo ID numérico
dadosOrdenados = [...dados].sort(
    (a, b) => Number((a.dimensoes[chaveNumerica])) - Number((b.dimensoes[chaveNumerica]))
);`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`// 2. Extrai apenas os valores formatados para o Plot
dadosGraficoLinhasFormatados = dadosOrdenados.map((d) => ({
    // Usar a chave de texto para o eixo X
    [chaveTexto]: d.dimensoes[chaveTexto], 
    valor: d.valor
}));`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`// 3. Define a ordem do domínio para garantir que o eixo X siga a ordem do ano.
domainOrder = dadosOrdenados.map(d => String(d.dimensoes[chaveTexto]));
                    `}
                </pre>
            </>
        )
    } else {
        return (
            <>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {`// 🔹 Prepara os dados em formato genérico
dadosFormatados = dados.map((d) => ({
    ...d.dimensoes,
    valor: d.valor,
}));`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {`// 🔹 Identifica dimensões
dimensoes = Object.keys(dados[0]?.dimensoes || {});`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {`primeiraDim = dimensoes[0];`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`segundaDim = dimensoes[1];`}
                </pre>
                <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                    {`terceiraDim = dimensoes[2];`}
                </pre>
            </>
        )
    }
}


export default function ChartInformation({pergunta, dados, tipo}: ChartInformation) {
    return (
        <>
            <p>A pergunta que gerou esse gráfico foi:</p>
            <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {pergunta}
            </pre>

            <p>Os dados para gerar esse gráfico foram:</p>
            <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {`dados = ` + dados}
            </pre>

            <p>O código para gerar esse gráfico foi:</p>
            <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {`// importar a biblioteca Plot\n`}
                {`import {Plot} from "@observablehq/plot"`}
            </pre>
            
            {intermediateCode(tipo)}
            
            <pre className="text-xs bg-gray-100 p-3 rounded whitespace-pre-wrap max-h-[300px] overflow-auto">
                {codeGraph(tipo)}
            </pre>
        </>
    )
}