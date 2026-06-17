import * as Plot from "@observablehq/plot";
import { createElement as h } from "react";
export default function PlotFigure({ options }) {
    return Plot.plot({ ...options, document: new Document() }).toHyperScript();
}
class Window {
    document;
    Event;
    constructor(document) {
        this.Event = globalThis.Event;
        this.document = document;
    }
}
class Document {
    documentElement;
    defaultView;
    constructor() {
        this.documentElement = new Element(this, "html");
        this.defaultView = new Window(this);
    }
    createElementNS(namespace, tagName) {
        return new Element(this, tagName);
    }
    createElement(tagName) {
        return new Element(this, tagName);
    }
    createTextNode(value) {
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
    setProperty() { }
    removeProperty() { }
}
class Element {
    ownerDocument;
    tagName;
    attributes;
    children;
    parentNode;
    _style = Style.empty;
    constructor(ownerDocument, tagName) {
        this.ownerDocument = ownerDocument;
        this.tagName = tagName;
        this.attributes = {};
        this.children = [];
        this.parentNode = null;
    }
    setAttribute(name, value) {
        this.attributes[name] = String(value);
    }
    setAttributeNS(namespace, name, value) {
        this.setAttribute(name, value);
    }
    getAttribute(name) {
        return this.attributes[name];
    }
    getAttributeNS(name) {
        return this.getAttribute(name);
    }
    hasAttribute(name) {
        return name in this.attributes;
    }
    hasAttributeNS(name) {
        return this.hasAttribute(name);
    }
    removeAttribute(name) {
        delete this.attributes[name];
    }
    removeAttributeNS(namespace, name) {
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
    append(...children) {
        for (const child of children) {
            this.appendChild(child?.ownerDocument
                ? child
                : this.ownerDocument.createTextNode(String(child)));
        }
    }
    appendChild(child) {
        this.children.push(child);
        child.parentNode = this;
        return child;
    }
    insertBefore(child, after) {
        if (after == null) {
            this.children.push(child);
        }
        else {
            const i = this.children.indexOf(after);
            if (i < 0)
                throw new Error("insertBefore reference node not found");
            this.children.splice(i, 0, child);
        }
        child.parentNode = this;
        return child;
    }
    querySelector() {
        return null;
    }
    querySelectorAll() {
        return [];
    }
    set textContent(value) {
        this.children = [this.ownerDocument.createTextNode(value)];
    }
    // **Setter e getter de style corrigidos**
    set style(value) {
        if (typeof value === "string") {
            this.attributes.style = value;
        }
        else {
            this._style = value;
        }
    }
    get style() {
        return this._style;
    }
    toHyperScript() {
        return h(this.tagName, this.attributes, this.children.map((c) => c.toHyperScript()));
    }
}
class TextNode {
    ownerDocument;
    nodeValue;
    constructor(ownerDocument, nodeValue) {
        this.ownerDocument = ownerDocument;
        this.nodeValue = String(nodeValue);
    }
    toHyperScript() {
        return this.nodeValue;
    }
}
