import * as Plot from "@observablehq/plot";
import { createElement as h } from "react";

interface PlotFigureProps {
  options: any; // você pode refinar isso depois com os tipos do Plot
}

export default function PlotFigure({ options }: PlotFigureProps) {
  return (Plot.plot({ ...options, document: new Document() }) as any).toHyperScript();
}


class Window {
  document: Document;
  Event: typeof globalThis.Event;

  constructor(document: Document) {
    this.Event = globalThis.Event;
    this.document = document;
  }
}

class Document {
  documentElement: Element;
  defaultView: Window;

  constructor() {
    this.documentElement = new Element(this, "html");
    this.defaultView = new Window(this);
  }

  createElementNS(namespace: string, tagName: string) {
    return new Element(this, tagName);
  }

  createElement(tagName: string) {
    return new Element(this, tagName);
  }

  createTextNode(value: string) {
    return new TextNode(this, value);
  }

  querySelector() {
    return null;
  }

  querySelectorAll() {
    return [];
  }
}

class Style {
  static empty = new Style();
  setProperty() {}
  removeProperty() {}
}

class Element {
  ownerDocument: Document;
  tagName: string;
  attributes: Record<string, string>;
  children: (Element | TextNode)[]; 
  parentNode: Element | null;
  private _style: Style = Style.empty;

  constructor(ownerDocument: Document, tagName: string) {
    this.ownerDocument = ownerDocument;
    this.tagName = tagName;
    this.attributes = {};
    this.children = [];
    this.parentNode = null;
  }

  setAttribute(name: string, value: string) {
    this.attributes[name] = String(value);
  }

  setAttributeNS(namespace: string, name: string, value: string) {
    this.setAttribute(name, value);
  }

  getAttribute(name: string) {
    return this.attributes[name];
  }

  getAttributeNS(name: string) {
    return this.getAttribute(name);
  }

  hasAttribute(name: string) {
    return name in this.attributes;
  }

  hasAttributeNS(name: string) {
    return this.hasAttribute(name);
  }

  removeAttribute(name: string) {
    delete this.attributes[name];
  }

  removeAttributeNS(namespace: string, name: string) {
    this.removeAttribute(name);
  }

  addEventListener() {
    // ignorado; interação precisa de DOM real
  }

  removeEventListener() {
    // ignorado; interação precisa de DOM real
  }

  dispatchEvent() {
    // ignorado; interação precisa de DOM real
  }

  append(...children: (Element | TextNode | string)[]) {
    for (const child of children) {
      this.appendChild(
        (child as any)?.ownerDocument
          ? (child as Element | TextNode)
          : this.ownerDocument.createTextNode(String(child))
      );
    }
  }

  appendChild(child: Element | TextNode) {
    this.children.push(child);
    (child as any).parentNode = this;
    return child;
  }

  insertBefore(child: Element | TextNode, after: Element | null) {
    if (after == null) {
      this.children.push(child);
    } else {
      const i = this.children.indexOf(after);
      if (i < 0) throw new Error("insertBefore reference node not found");
      this.children.splice(i, 0, child);
    }
    (child as any).parentNode = this;
    return child;
  }

  querySelector() {
    return null;
  }

  querySelectorAll() {
    return [];
  }

  set textContent(value: string) {
    this.children = [this.ownerDocument.createTextNode(value)];
  }

  // **Setter e getter de style corrigidos**
  set style(value: string | Style) {
    if (typeof value === "string") {
      this.attributes.style = value;
    } else {
      this._style = value;
    }
  }

  get style(): Style {
    return this._style;
  }

  toHyperScript(): any {
    return h(
      this.tagName,
      this.attributes,
      this.children.map((c) => c.toHyperScript())
    );
  }
}


class TextNode {
  ownerDocument: Document;
  nodeValue: string;

  constructor(ownerDocument: Document, nodeValue: string) {
    this.ownerDocument = ownerDocument;
    this.nodeValue = String(nodeValue);
  }

  toHyperScript() {
    return this.nodeValue;
  }
}
