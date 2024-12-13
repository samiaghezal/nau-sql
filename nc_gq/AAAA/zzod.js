const schema = z.array(
  z.union([
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.string()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.string(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.string(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      )
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      )
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      )
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      )
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      ),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.null(),
                        ofType: z.object({
                          kind: z.string(),
                          name: z.string(),
                          ofType: z.null()
                        })
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.string(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.null(),
                        ofType: z.object({
                          kind: z.string(),
                          name: z.string(),
                          ofType: z.null()
                        })
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.null(),
                        ofType: z.object({
                          kind: z.string(),
                          name: z.string(),
                          ofType: z.null()
                        })
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.null(),
                        ofType: z.object({
                          kind: z.string(),
                          name: z.string(),
                          ofType: z.null()
                        })
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.string(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.string(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.null(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.null(),
                      ofType: z.object({
                        kind: z.string(),
                        name: z.string(),
                        ofType: z.null()
                      })
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.string()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.string()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.string()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.string(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.string()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.string()
                }),
                z.object({
                  name: z.string(),
                  description: z.null(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(
              z.union([
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  }),
                  defaultValue: z.string(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                }),
                z.object({
                  name: z.string(),
                  description: z.string(),
                  type: z.object({
                    kind: z.string(),
                    name: z.null(),
                    ofType: z.object({
                      kind: z.string(),
                      name: z.string(),
                      ofType: z.null()
                    })
                  }),
                  defaultValue: z.null(),
                  isDeprecated: z.boolean(),
                  deprecationReason: z.null()
                })
              ])
            ),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          type: z.object({
            kind: z.string(),
            name: z.string(),
            ofType: z.null()
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            })
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            })
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.null(),
      inputFields: z.null(),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.array(
        z.object({ kind: z.string(), name: z.string(), ofType: z.null() })
      )
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.string(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.object({
          name: z.string(),
          description: z.null(),
          args: z.array(z.unknown()),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            })
          }),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.object({
          name: z.string(),
          description: z.string(),
          type: z.object({
            kind: z.string(),
            name: z.null(),
            ofType: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            })
          }),
          defaultValue: z.null(),
          isDeprecated: z.boolean(),
          deprecationReason: z.null()
        })
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.null(),
      fields: z.null(),
      inputFields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            defaultValue: z.null(),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      interfaces: z.null(),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.string(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(
              z.object({
                name: z.string(),
                description: z.null(),
                type: z.object({
                  kind: z.string(),
                  name: z.string(),
                  ofType: z.null()
                }),
                defaultValue: z.string(),
                isDeprecated: z.boolean(),
                deprecationReason: z.null()
              })
            ),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.string(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    }),
    z.object({
      kind: z.string(),
      name: z.string(),
      description: z.string(),
      fields: z.array(
        z.union([
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.string(),
                ofType: z.null()
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.string(),
              ofType: z.null()
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          }),
          z.object({
            name: z.string(),
            description: z.null(),
            args: z.array(z.unknown()),
            type: z.object({
              kind: z.string(),
              name: z.null(),
              ofType: z.object({
                kind: z.string(),
                name: z.null(),
                ofType: z.object({
                  kind: z.string(),
                  name: z.null(),
                  ofType: z.object({
                    kind: z.string(),
                    name: z.string(),
                    ofType: z.null()
                  })
                })
              })
            }),
            isDeprecated: z.boolean(),
            deprecationReason: z.null()
          })
        ])
      ),
      inputFields: z.null(),
      interfaces: z.array(z.unknown()),
      enumValues: z.null(),
      possibleTypes: z.null()
    })
  