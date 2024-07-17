export const idlFactory = ({ IDL }) => {
  return IDL.Service({
    'get_message' : IDL.Func([], [IDL.Vec(IDL.Int32)], ['query']),
  });
};
export const init = ({ IDL }) => { return []; };
