import * as Plot from "@observablehq/plot";
import PlotFigure from "./PlotFigure";
import { useEffect, useState } from "react";

interface Dado {
  dimensoes: Record<string, string | number>;
  valor: number;
}

interface PlotGenericProps {
  tipo: string;
  dados: Dado[];
  tamanho?: number | null;
}

function temValores(dados: any, dim: any) {
  if (!dim) return false; // não existe
  return dados.some((d:any) => d.dimensoes[dim] !== undefined && d.dimensoes[dim] !== null);
}

export default function PlotGeneric({ tipo, dados, tamanho=null }: PlotGenericProps) {
  const [brasil, setBrasil] = useState<any>(null);

  // 🔹 Busca do mapa do Brasil (necessário para coropléticos)
  useEffect(() => {
    if (tipo === "mapas_coropleticos") {
      fetch(
        "https://raw.githubusercontent.com/giuliano-macedo/geodata-br-states/refs/heads/main/geojson/br_states.json"
      )
        .then((res) => res.json())
        .then((data) => setBrasil(data))
        .catch((error) => console.error("Erro ao carregar mapa:", error));
    }
  }, [tipo]);

  // 🔹 Prepara os dados em formato genérico
  const dadosFormatados = dados.map((d) => ({
    ...d.dimensoes,
    valor: d.valor,
  }));

  // 🔹 Identifica dimensões
  const dimensoes = Object.keys(dados[0]?.dimensoes || {});
  const primeiraDim = dimensoes[0];
  const segundaDim = dimensoes[1];
  const terceiraDim = dimensoes[2];

  const fillDim =
          temValores(dados, terceiraDim) ? terceiraDim :
          temValores(dados, segundaDim)  ? segundaDim  :
          primeiraDim;

  // 🔹 Função que renderiza o gráfico de acordo com o tipo
  const renderPlot = () => {
    switch (tipo) {
      case "grafico_barras_horizontal":
        return (
          <PlotFigure
            options={{
              width: tamanho ?? tamanho ?? 530,
              height: tamanho ?? 530,
              marks: [
                Plot.barX(dadosFormatados, {
                  x: "valor",
                  y: primeiraDim,
                  fill: "steelblue",
                }),
              ],
              x: { grid: true },
              marginLeft: 120,
            }}
          />
        );

      case "grafico_barras_vertical":
        return (
          <PlotFigure
            options={{
              width: tamanho ?? 530,
              height: tamanho ?? 530,
              marks: [
                Plot.barY(dadosFormatados, {
                  x: primeiraDim,
                  y: "valor",
                  fill: "steelblue",
                }),
              ],
              x: { tickRotate: -45 },
              marginBottom: 100,
            }}
          />
        );

      case "graficos_linhas":
        const dims = dados[0].dimensoes;
        
        // Detecta automaticamente as chaves de dimensão
        const chaveNumerica = Object.keys(dims).find(k => typeof dims[k] === "number"); // Ex: "id_ano"
        const chaveTexto = Object.keys(dims).find(k => typeof dims[k] === "string"); // Ex: "Ano de Notificação"
        
        if (!chaveNumerica || !chaveTexto) return null; // Proteção
        
        // 1. Ordena os dados pelo ID numérico (ex: 2020, 2021, 2022...)
        const dadosOrdenados = [...dados].sort(
            (a, b) => (a.dimensoes[chaveNumerica] as number) - (b.dimensoes[chaveNumerica] as number)
        ); 
        
        // 2. Extrai apenas os valores formatados para o Plot
        const dadosGraficoLinhasFormatados = dadosOrdenados.map((d: Dado) => ({
            // Usar a chave de texto para o eixo X
            [chaveTexto]: d.dimensoes[chaveTexto], 
                    valor: d.valor
        }));
                
        // 3. Define a ordem do domínio para garantir que o eixo X siga a ordem do ano.
        const domainOrder = dadosOrdenados.map(d => d.dimensoes[chaveTexto] as string);
        
        return (
            <PlotFigure
                 options={{
                    width: tamanho ?? 530,
                    height: tamanho ?? 530,
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
                }}
            />
        );

      case "mapas_coropleticos":
        if (!brasil) return <p>Carregando mapa...</p>;
        return (
          <PlotFigure
            options={{
              width: tamanho ?? 530,
              height: tamanho ?? 530,
              axis: null,
              color: {
                type: "quantize",
                scheme: "blues",
                label: "Valor",
                legend: true,
              },
              marks: [
                Plot.geo(brasil, {
                  fill: (feature: any) => {
                    const estado = feature.properties.Estado;
                    return dados.find(
                      (d) => Object.values(d.dimensoes)[0] === estado
                    )?.valor;
                  },
                  stroke: "lightgray",
                }),
              ],
            }}
          />
        );

      case "graficos_com_proporcao":
        return (
          <PlotFigure
            options={{
              width: tamanho ?? 530,
              height: tamanho ?? 530,
              x: { label: primeiraDim, tickRotate: -40 },
              y: { label: "Valor" },
              color: { legend: true },
              marks: [
                Plot.barY(dadosFormatados, {
                  x: primeiraDim,
                  y: "valor",
                  fill: fillDim,
                  
                }),
              ],
              marginBottom: 120,
            }}
          />
        );

      default:
        return <p>Tipo de gráfico não suportado.</p>;
    }
  };

  return <>{renderPlot()}</>;
}
