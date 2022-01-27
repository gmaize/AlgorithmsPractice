const Node = require('./Node')
const zero = new Node(0)
const one = new Node(1)
const two = new Node(2)
const three = new Node(3)
const four = new Node(4)
const five = new Node(5)
const six = new Node(6)
const nodes = [zero, one, two, three, four, five]

five.addNeighbor(zero)
five.addNeighbor(two)
four.addNeighbor(zero)
four.addNeighbor(one)
two.addNeighbor(three)
three.addNeighbor(one)

getConnectedComponents(nodes)

function getConnectedComponents(nodes) {
    const visited = {}
    const components = []
    for (var node of nodes) {
        if (visited[node.id]) continue
        const component = []
        visit(node, component, visited)
        components.push(component)
    }
    console.log(components)
}

function visit(node, component, visited) {
    if (visited[node.id]) return
    visited[node.id] = true
    component.push(node)
    for (var neighbor of node.neighbors) {
        visit(neighbor, component, visited)
    }
}