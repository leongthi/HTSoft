//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace CR_API.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class L_ReportParam
    {
        public System.Guid ReportID { get; set; }
        public int ID { get; set; }
        public int Index { get; set; }
        public string ParamName { get; set; }
        public string ParamDescripsion { get; set; }
        public string ParamType { get; set; }
        public Nullable<bool> IsMandostory { get; set; }
        public string DefaultValue { get; set; }
        public string Notes { get; set; }
        public string Caption { get; set; }
        public string Option { get; set; }
        public string ValueType { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
        public string CreatedBy { get; set; }
        public Nullable<System.DateTime> ModifiedOn { get; set; }
        public string ModifiedBy { get; set; }
        public Nullable<int> STT { get; set; }
    }
}