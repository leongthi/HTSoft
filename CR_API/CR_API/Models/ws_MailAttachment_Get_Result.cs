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
    
    public partial class ws_MailAttachment_Get_Result
    {
        public Nullable<System.Guid> MailMessageKey { get; set; }
        public string FileName { get; set; }
        public string ContentType { get; set; }
        public string Content { get; set; }
        public Nullable<System.DateTime> CreatedOn { get; set; }
    }
}
